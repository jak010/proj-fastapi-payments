APPLICATION=src.proj_fastapi_payments.app:application


run.dev.fastapi:
	poetry run uvicorn $(APPLICATION) --factory --reload