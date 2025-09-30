import streamlit as st
import requests

def fetch_countries_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:  # check if list is not empty
            country_data = data[0]
            name = country_data.get("name", {}).get("common", "N/A")
            capital = country_data.get("capital", ["N/A"])[0]
            population = country_data.get("population", "N/A")
            area = country_data.get("area", "N/A")
            region = country_data.get("region", "N/A")
            subregion = country_data.get("subregion", "N/A")
            languages = country_data.get("languages", {}).values()
            languages = ', '.join(languages) if languages else "N/A"
            currencies = country_data.get("currencies", {}).values()
            currencies = ', '.join([f"{curr['name']} ({curr['symbol']})" for curr in currencies]) if currencies else "N/A"
            flags = country_data.get("flags", {}).get("png", "N/A")
            return {
                "name": name,
                "capital": capital,
                "population": population,
                "area": area,
                "region": region,
                "subregion": subregion,
                "languages": languages,
                "currencies": currencies,
                "flags": flags
            }
    return None
    
def main():
    st.title("Country Information Cards")
    st.write("Enter a country name to get its information.")

    country_name = st.text_input("Country Name", "")

    if st.button("Country Information"):
        if country_name:
            with st.spinner("Fetching data..."):
                country_data = fetch_countries_data(country_name)
            if country_data:
                st.image(country_data["flags"], width=100)
                st.subheader(country_data["name"])
                st.write(f"**Capital:** {country_data['capital']}")
                st.write(f"**Population:** {country_data['population']}")
                st.write(f"**Area:** {country_data['area']} km²")
                st.write(f"**Region:** {country_data['region']}")
                st.write(f"**Subregion:** {country_data['subregion']}")
                st.write(f"**Languages:** {country_data['languages']}")
                st.write(f"**Currencies:** {country_data['currencies']}")
            else:
                st.error("Country not found. Please check the name and try again.")
        else:
            st.warning("Please enter a country name.")

if __name__ == "__main__":
    main()
