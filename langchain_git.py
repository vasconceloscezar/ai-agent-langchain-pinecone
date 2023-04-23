from git import Repo


def clone_repo():
    repo = Repo.clone_from(
        # "https://github.com/hwchase17/langchain", to_path="./example_data/test_repo1"
        # "https://github.com/lightaime/camel",
        "https://github.com/Kamona-WD/kwd-dashboard/tree/rewrite",
        to_path="./example_data/dash-repo-tailwind",
    )
    branch = repo.head.reference


from langchain.document_loaders import GitLoader

loader = GitLoader(repo_path="./example_data/dash-repo-tailwind/", branch="master")
data = loader.load()

len(data)
print(data[0])
