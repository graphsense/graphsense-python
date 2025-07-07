-include .env

generate-openapi-client:
	@echo "Downloading openapi.json..."
	curl -s "$(GS_REST_SERVICE_URL)/openapi.json" -o openapi.json.tmp
	@echo "Modifying server URL to production..."
	jq '.servers[0].url = "https://api.ikna.io"' openapi.json.tmp > openapi.json.modified
	@echo "Generating client..."
	docker run --rm \
		-v "${PWD}:/build:Z" \
		-v "${PWD}/templates:/templates:Z" \
		openapitools/openapi-generator-cli:v5.2.1 \
		generate -i /build/openapi.json.modified \
		-g python \
		-t /templates \
		-o /build \
		--additional-properties=packageName=graphsense \
		--additional-properties=projectName=graphsense-python
	@echo "Cleaning up temporary files..."
	rm -f openapi.json.tmp openapi.json.modified

run-examples:
	API_KEY=$(API_KEY) python test_examples.py

.PHONY: generate-openapi-client run-examples
