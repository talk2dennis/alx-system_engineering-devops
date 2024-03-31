# 0x0F. Load balancer
> This repository contains bash script that configures and provisions nginx web servers and HAproxy loadbalancers.

## TASKS
### 0. Double the number of webservers
> configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!
> - Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
> - The name of the custom HTTP header must be ```X-Served-By```
> - The value of the custom HTTP header must be the hostname of the server Nginx is running on
> - ```File: 0-custom_http_response_header```

### 1. Install your load balancer
> - Configure HAproxy so that it send traffic to ```web-01``` and ```web-02```
> - Distribute requests using a roundrobin algorithm
> - Make sure that HAproxy can be managed via an init script
> - File: ```1-install_load_balancer```

### Add a custom HTTP header with Puppet
> Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
> - The name of the custom HTTP header must be X-Served-By
> - The value of the custom HTTP header must be the hostname of the server Nginx is running on
> - Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task
