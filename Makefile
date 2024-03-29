generate-openapi-client:
	docker run --rm \
		-v "${PWD}:/build:Z" \
		-v "${PWD}/templates:/templates:Z" \
		openapitools/openapi-generator-cli:v5.2.1 \
		generate -i "$(GS_REST_SERVICE_URL)/openapi.json" \
		-g python \
		-t /templates \
		-o /build \
		--additional-properties=packageName=graphsense \
		--additional-properties=projectName=graphsense-python


.PHONY: generate-openapi-client
