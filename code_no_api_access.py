# prompt user for input
input_filename = input(
    "Enter the name of the Python file (include .py extension) to use: ")

# Read file contents and store as string variable
with open(input_filename, "r") as file:
    input_file_contents = file.read()

# for testing purposes
input_file_contents = 'user input'

# create the prompt for api call
prompt = f"""Python 3

{input_file_contents}

Here is some python code, can you improve the format and explain what it does
"""

# call API

# response = openai.Completion.create(
#   model="gpt-3.5-turbo",
#   prompt=prompt,
#   temperature=0,
#   max_tokens=150,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0,
# )

# Define the filename and the string containing Python code
output_filename = input(
    "Enter the name of the Python file (include .py extension) to create: ")

# for testing purposes
response = 'test'

# Write the string to a file with .py extension
with open(output_filename, "w") as file:
    file.write(response)

print(f"Successfully wrote the Python code to {output_filename}")
