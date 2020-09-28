# challenges

## 2. Benford's Law

To run the solution:
1. Go to the project's directory in your terminal,
1. Build an image based off the supplied Dockerfile in project's root:
```
docker build --tag challenges .
```
2. Run the image, giving the new container a name of choice (needed to identify the container in the next step):
```
docker run --name challenges_container challenges
```
3. Copy the newly created PNG file from the container to project's directory:
```
docker cp challenges_container:/app/graph.png .
```
4. Open the 'graph.png' file to see the result.