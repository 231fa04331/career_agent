from utils.pdf_reader import extract_text_from_pdf
from graph import build_graph


def display_results(result):

    print("\n" + "=" * 80)
    print("CANDIDATE PROFILE")
    print("=" * 80)

    profile = result["profile"]

    print(f"Name       : {profile.name}")
    print(f"Experience : {profile.experience}")

    print("\nSkills:")
    for skill in profile.skills:
        print(f"  • {skill}")

    print("\nSuitable Roles:")
    for role in profile.roles:
        print(f"  • {role}")

    print("\nProjects:")
    for project in profile.projects:
        print(f"  • {project}")

    print("\n" + "=" * 80)
    print("SEARCH QUERY")
    print("=" * 80)

    print(result["search_query"])

    print("\n" + "=" * 80)
    print("TOP MATCHED JOBS")
    print("=" * 80)

    for index, job in enumerate(result["matched_jobs"], start=1):

        print(f"\nTop Match {index}")

        print(f"Title   : {job.title}")
        print(f"Company : {job.company}")
        print(f"Reason  : {job.reason}")
        print(f"URL     : {job.url}")

    print("\n" + "=" * 80)
    print("COVER LETTER")
    print("=" * 80)

    print(result["cover_letter"])


def main():

    graph = build_graph()

    print("=" * 80)
    print("Career Multi-Agent Assistant")
    print("=" * 80)

    while True:

        pdf_path = input("\nEnter Resume PDF Path: ").strip().strip('"')

        try:

            resume_text = extract_text_from_pdf(pdf_path)

        except Exception as e:

            print(f"\nError: {e}")

            continue

        initial_state = {

            "resume_text": resume_text,

            "profile": {},

            "search_query": "",

            "jobs": [],

            "matched_jobs": [],

            "cover_letter": ""

        }

        print("\nAnalyzing Resume...\n")

        result = graph.invoke(initial_state)

        display_results(result)

        again = input("\nAnalyze another resume? (y/n): ").lower()

        if again != "y":
            break

    print("\nThank you for using Career Agent!")


if __name__ == "__main__":
    main()