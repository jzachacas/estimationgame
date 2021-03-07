dist:
	cd client && npm run build

clean:
	rm -rf client/dist

release: dist
	tar -czvf estimo.tar.gz backend/requirements.txt backend/*.py Dockerfile\
	  swagger.yaml client/dist nginx.conf start.sh dogu.json README.md screenshot.png
