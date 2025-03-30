from scholarly import scholarly
import json

def extract_publications_scholarly(scholar_id):
    """
    Extracts publications from a Google Scholar profile using scholarly.

    Args:
        scholar_id (str): The Google Scholar ID of the author.

    Returns:
        list: A list of dictionaries, where each dictionary contains publication data.
    """

    try:
        author = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(author, sections=['publications'])
        publications = author['publications']

        results = []
        for pub in publications:
            pub = scholarly.fill(pub) #fill the publication object, to get the abstract.
            title = pub['bib'].get('title', 'N/A')
            authors = pub['bib'].get('author', 'N/A')
            year = pub['bib'].get('pub_year', 'N/A')
            abstract = pub['bib'].get('abstract', 'N/A')

            results.append({
                "title": title,
                "authors": authors,
                "year": year,
                "abstract": abstract
            })

        return results

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
scholar_id = "Ooigad8AAAAJ" # Replace with your Google Scholar ID
publications_data = extract_publications_scholarly(scholar_id)

if publications_data:
    with open("scholar_publications_scholarly.json", "w", encoding="utf-8") as f:
        json.dump(publications_data, f, ensure_ascii=False, indent=4)
    print("Publications extracted and saved to scholar_publications_scholarly.json")
else:
    print("Failed to extract publications.")