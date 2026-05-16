import logging
import os
import sys

from streamlit.web import cli as streamlit_cli


app_base_dir = os.path.abspath(os.path.dirname(__file__))
if app_base_dir not in sys.path:
    sys.path.insert(0, app_base_dir)

app_env = os.getenv("APP_ENV", "local")
DEFAULT_LOG_FILE_PATH = os.path.join(app_base_dir, "logs", "app.log")


def configure_logging() -> None:
    try:
        from common import logging_config
    except ImportError:
        os.makedirs(os.path.dirname(DEFAULT_LOG_FILE_PATH), exist_ok=True)
        logging.basicConfig(
            filename=os.path.abspath(DEFAULT_LOG_FILE_PATH),
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        )
        return

    logging_config.configure_logging(app_env, os.path.abspath(DEFAULT_LOG_FILE_PATH))


def main() -> None:
    configure_logging()
    frontend_path = os.path.join(app_base_dir, "frontend", "frontend.py")
    sys.argv = ["streamlit", "run", frontend_path]
    raise SystemExit(streamlit_cli.main())


if __name__ == "__main__":
    main()
