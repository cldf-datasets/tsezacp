# Releasing the Tsez Annotated Corpus

0. CLone repos and install dependencies:
   ```shell
   git clone https://github.com/cldf-datasets/tsezacp tsezacp-cldf
   cd tsezacp-cldf
   pip install -e .[test]
   ```
1. Re-create the CLDF:
   ```shell
   cldfbench makecldf cldfbench_tsezacp.py --glottolog-version v5.3 --with-zenodo --with-cldfreadme
   ```
2. Validate the CLDF:
   ```shell
   pytest
   ```
3. Re-create the README:
   ```shell
   cldfbench readme cldfbench_tsezacp.py
   ```
4. Commit, tag and push to origin.
5. Create the corresponding release on GitHub, thereby triggering upload to Zenodo.
6. Copy the DOI assigned by Zenodo into the release description on GitHub.
