client = weaviate.Client(
    url=os.environ["WEAVIATE_URL"],
    auth_client_secret=auth_config,
    additional_headers={"X-Cohere-Api-Key": os.environ["COHERE_API_KEY"]},
    startup_period=30,  # Adjust to allow more time
)