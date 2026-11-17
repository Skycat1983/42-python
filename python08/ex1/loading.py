#!/usr/bin/env python3

# importlib is a python standard-library module for importing other modules
# dynamically from names stored as strings
# here it lets the dependency loop report missing packages gracefully instead
# of top-level imports stopping the program immediately
import importlib
import sys
from typing import Any

REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
}

#   python3 -m venv matrix_env
#   source matrix_env/bin/activate
#   python3 -m pip install -r requirements.txt
#   poetry install


def load_dependencies() -> dict[str, Any] | None:
    loaded: dict[str, Any] = {}
    missing: list[str] = []

    print("Checking dependencies:")
    for package, purpose in REQUIRED_PACKAGES.items():
        try:
            # example return for "numpy": the imported numpy module object
            module = importlib.import_module(package)
        except ImportError:
            missing.append(package)
            print(f"[MISSING] {package} - {purpose} unavailable")
        else:
            loaded[package] = module
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {package} ({version}) - {purpose} ready")

    if missing:
        print("\nUnable to analyze data. Missing: " + ", ".join(missing))
        print("\nInstall with pip:")
        print("  python -m pip install -r requirements.txt")
        print("\nOr install with Poetry:")
        print("  poetry install")
        print("  poetry run python loading.py")
        return None

    return loaded


def show_package_manager_comparison() -> None:
    print("\nDependency management comparison:")
    print("- pip reads requirements.txt and installs its listed packages.")
    print("- Poetry reads pyproject.toml and resolves dependencies into a")
    print("  reproducible lock file.")
    print("- Both approaches install the same analysis dependencies here.")


def analyze_matrix_data(modules: dict[str, Any]) -> str:
    # generate, summarize, and plot simulated matrix signal data.
    np = modules["numpy"]  # resolve numpy dependency
    pd = modules["pandas"]  # resolve pandas dependency
    matplotlib = modules["matplotlib"]  # resolve matplotlib dependency

    matplotlib.use("Agg")  # non-interactive backend for file output
    # pyplot is imported only after selecting the non-interactive "Agg" backend
    pyplot = importlib.import_module("matplotlib.pyplot")
    # delayed pyplot import

    print("\nAnalyzing Matrix data...")
    generator = np.random.default_rng(seed=42)  # seeded rng
    point_count = 1000  # fixed number of samples
    timestamps = np.arange(point_count)  # create x-axis range
    signal = generator.normal(  # generate numeric signal
        loc=50.0,
        scale=12.0,
        size=point_count,
    )
    anomaly_limit = 72.0  # anomaly threshold value

    frame = pd.DataFrame(
        {
            "timestamp": timestamps,
            "signal_strength": signal,
            "is_anomaly": signal > anomaly_limit,
        }
    )  # build dataframe from arrays
    print(f"Processing {len(frame)} data points...")  # log row count
    print(f"Average signal: {frame['signal_strength'].mean():.2f}")
    # average signal
    print(f"Strongest signal: {frame['signal_strength'].max():.2f}")
    # peak signal
    print(f"Anomalies detected: {int(frame['is_anomaly'].sum())}")
    # anomaly count

    print("Generating visualization...")
    figure, axis = pyplot.subplots(figsize=(10, 5))  # create canvas and axes
    axis.plot(
        frame["timestamp"],
        frame["signal_strength"],
        color="#18a558",
        linewidth=0.8,
        label="Matrix signal",  # draw full signal line
    )
    anomalies = frame[frame["is_anomaly"]]  # keep only anomaly rows
    axis.scatter(
        anomalies["timestamp"],
        anomalies["signal_strength"],
        color="#d62828",
        s=18,
        label="Anomaly",  # overlay anomaly markers
    )
    axis.axhline(
        anomaly_limit,
        color="#f4a261",
        linestyle="--",
        label="Anomaly threshold",  # draw anomaly cutoff line
    )
    axis.set(  # set chart labels
        title="Matrix Signal Analysis",
        xlabel="Time step",
        ylabel="Signal strength",
    )
    axis.legend()  # show legend
    figure.tight_layout()  # compact layout to avoid overlap

    output_path = "matrix_analysis.png"  # output file path
    figure.savefig(output_path, dpi=150)  # save plot image
    pyplot.close(figure)  # release figure resources
    return output_path


def main() -> int:
    print("LOADING STATUS: Loading programs...")
    modules = load_dependencies()
    show_package_manager_comparison()
    if modules is None:
        return 1

    try:
        output_path = analyze_matrix_data(modules)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"\nAnalysis failed safely: {error}", file=sys.stderr)
        return 1

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
