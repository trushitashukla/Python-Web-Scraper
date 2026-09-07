import streamlit as st
from scraper import scrape_website
import pandas as pd

st.set_page_config(
    page_title="Web Scraper",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Web Scraper & Data Extractor")
st.write("Extract, search and download information from a webpage.")

# URL input
url = st.text_input(
    "🌐 Enter Website URL",
    placeholder="https://books.toscrape.com/"
)

if st.button("🔍 Scrape Website", use_container_width=True):

    if url:

        try:
            with st.spinner("Scraping website..."):
                data = scrape_website(url)

            st.session_state["data"] = data
            st.session_state["url"] = url

            st.success("✅ Website scraped successfully!")

        except Exception as e:
            st.error(f"❌ Unable to scrape the website: {e}")

    else:
        st.warning("⚠️ Please enter a website URL.")


# Display results
if "data" in st.session_state:

    data = st.session_state["data"]

    st.divider()

    # Page information
    st.subheader("📄 Page Information")
    st.write(data["title"])

    # Summary
    st.subheader("📊 Scraping Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "📰 Headings",
        len(data["headings"])
    )

    col2.metric(
        "🔗 Links",
        len(data["links"])
    )

    col3.metric(
        "🖼️ Images",
        len(data["images"])
    )

    st.divider()

    # Search
    st.subheader("🔍 Search Scraped Data")

    search = st.text_input(
        "Search keyword",
        placeholder="Example: catalogue"
    )

    # Filter data
    filtered_headings = [
        heading
        for heading in data["headings"]
        if search.lower() in heading.lower()
    ]

    filtered_links = [
        link
        for link in data["links"]
        if search.lower() in link.lower()
    ]

    filtered_images = [
        image
        for image in data["images"]
        if search.lower() in image.lower()
    ]

    # Tabs
    tab1, tab2, tab3 = st.tabs([
        "📰 Headings",
        "🔗 Links",
        "🖼️ Images"
    ])

    # Headings tab
    with tab1:

        st.write(
            f"Found **{len(filtered_headings)}** matching headings."
        )

        if filtered_headings:
            heading_df = pd.DataFrame(
                filtered_headings,
                columns=["Heading"]
            )

            st.dataframe(
                heading_df,
                use_container_width=True,
                hide_index=True
            )

        else:
            st.info("No matching headings found.")

    # Links tab
    with tab2:

        st.write(
            f"Found **{len(filtered_links)}** matching links."
        )

        if filtered_links:
            link_df = pd.DataFrame(
                filtered_links,
                columns=["Link"]
            )

            st.dataframe(
                link_df,
                use_container_width=True,
                hide_index=True
            )

        else:
            st.info("No matching links found.")

    # Images tab
    with tab3:

        st.write(
            f"Found **{len(filtered_images)}** matching images."
        )

        if filtered_images:
            image_df = pd.DataFrame(
                filtered_images,
                columns=["Image URL"]
            )

            st.dataframe(
                image_df,
                use_container_width=True,
                hide_index=True
            )

        else:
            st.info("No matching images found.")

    st.divider()

    # CSV Export
    rows = []

    for heading in data["headings"]:
        rows.append(["Heading", heading])

    for link in data["links"]:
        rows.append(["Link", link])

    for image in data["images"]:
        rows.append(["Image", image])

    df = pd.DataFrame(
        rows,
        columns=["Type", "Data"]
    )

    csv = df.to_csv(index=False)

    st.download_button(
        label="💾 Download All Data as CSV",
        data=csv,
        file_name="scraped_data.csv",
        mime="text/csv",
        use_container_width=True
    )