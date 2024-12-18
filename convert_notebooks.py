import os
import nbformat
from nbconvert import PythonExporter, NotebookExporter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_exporter(from_format: str, to_format: str):

    if (from_format.lower() in ["python", ".py", "py"]) and (
        to_format.lower() in ["notebook", "ipynb", ".ipynb"]
    ):
        exporter = PythonExporter()  # Convert to Python

    elif (to_format.lower() in ["python", ".py", "py"]) and (
        from_format.lower() in ["notebook", "ipynb", ".ipynb"]
    ):
        exporter = NotebookExporter()  # Convert to Python
    else:
        raise ValueError("Can't convert {from_format} to {to_format}!")
    return exporter


def convert_notebook(notebook_path: Path, from_format: str, to_format: str):
    """
    Convert a single notebook to Python script.

    Args:
        notebook_path (Path): Path to the notebook file
    """
    try:
        output_path = notebook_path.with_suffix(".py")

        if output_path.exists():  # Skip if Python file is newer than notebook
            if output_path.stat().st_mtime > notebook_path.stat().st_mtime:
                logger.info(
                    f"Skipping {notebook_path.name} - Python file is up to date"
                )
                return

        with open(notebook_path) as f:  # Read the notebook
            notebook = nbformat.read(f, as_version=4)

        exporter = get_exporter(from_format, to_format)
        out, _ = exporter.from_notebook_node(notebook)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(out)  # Write the Python file

        logger.info(f"Successfully converted {notebook_path.name}")

    except Exception as e:
        logger.error(f"Error converting {notebook_path.name}: {str(e)}")


def convert_notebooks_in_directory(
    directory_path: str, format_from: str, format_to: str, max_workers: int = 4
) -> None:
    root_path = Path(directory_path)  # Convert string path to Path object
    notebook_files = list(root_path.rglob("*.ipynb"))  # Find all notebook files

    if not notebook_files:
        logger.warning(f"No notebook files found in {directory_path}")
        return

    logger.info(f"Found {len(notebook_files)} notebook files")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:  # parallelize
        for f in notebook_files:
            executor.map(convert_notebook, f, format_from, format_to)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert Jupyter notebooks to Python scripts recursively"
    )
    parser.add_argument("root", help="Root directory containing notebooks", default=".")
    parser.add_argument(
        "-f", "--format_from", help="Format to convert from", default="ipynb"
    )
    parser.add_argument("-t", "--format_to", help="Format to convert to", default="py")
    parser.add_argument(
        "--workers", help="Number of parallel workers", type=int, default=4
    )

    args = parser.parse_args()

    # Convert notebooks
    convert_notebooks_in_directory(
        args.root, args.format_from, args.format_to, args.workers
    )


if __name__ == "__main__":
    main()
