FROM ubuntu:20.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y ruby=1:2.7+1 --allow-downgrades
RUN apt-get install -y ruby-augeas
RUN apt-get install -y ruby-shadow
RUN apt-get install -y puppet
RUN gem install puppet-lint

CMD ["puppet-lint", "--version"]
CMD ["/bin/bash"]
