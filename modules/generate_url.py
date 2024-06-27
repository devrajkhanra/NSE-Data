def generate_url(date_input: str, base_url: str) -> str:
    # Replace placeholder with user input
    final_url = base_url.replace("date", date_input)

    # Print the final URL
    return final_url
