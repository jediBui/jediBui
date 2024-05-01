input_file_name = "servers.txt"
with open(input_file_name, "r") as file:
  server_list = file.read().splitlines()

result_string = ""
for server in server_list:
  print(server)
  result_string += server + ".s02.chevron.net\n"

output_file_name = "moba.txt"
with open(output_file_name, "w") as file:
  file.write(result_string)