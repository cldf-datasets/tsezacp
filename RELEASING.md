# Releasing the Tsez Annotated Corpus

1. Re-create the CLDF:
   ```shell
   $ cldfbench makecldf cldfbench_tsezacp.py --glottolog-version v4.6 --with-zenodo --with-cldfreadme
   ```
2. Validate the CLDF:
   ```shell
   $ pytest
   ```
3. Re-create the README:
   ```shell
   $ cldfbench readme cldfbench_tsezacp.py
   ```
4. Commit, tag and push to origin.
5. Create the corresponding release on GitHub, thereby triggering upload to Zenodo.
6. Copy the DOI assigned by Zenodo into the release description on GitHub.
