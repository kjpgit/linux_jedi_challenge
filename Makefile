run:
	docker build -t jedi .
	docker run -it --rm jedi

push:
	aws --profile=personal ecr-public get-login-password --region us-east-1 | \
	    docker login --username AWS --password-stdin public.ecr.aws/p5e0b0g4
	docker build -t kjpgit/linux-jedi-challenge .
	docker tag kjpgit/linux-jedi-challenge:latest \
	    public.ecr.aws/p5e0b0g4/kjpgit/linux-jedi-challenge:latest
	docker push public.ecr.aws/p5e0b0g4/kjpgit/linux-jedi-challenge:latest
