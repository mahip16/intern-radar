import os

from sqlalchemy import create_engine, text


def main() -> None:
    engine = create_engine(os.environ["DATABASE_URL"])
    with engine.connect() as conn:
        version = conn.execute(text("SELECT version()")).scalar()
    print(f"Connected: {version}")


if __name__ == "__main__":
    main()