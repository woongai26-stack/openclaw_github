import os
import subprocess
import shutil

def sync_openclaw_docs_zip():
    """
    Downloads the latest OpenClaw documentation as a zip file,
    unzips it, and cleans up. This is more reliable than git clone
    in non-interactive environments.
    """
    base_path = "/Users/woongsmacmini/.openclaw/workspace/reference"
    zip_path = os.path.join(base_path, "openclaw_docs.zip")
    repo_dir = os.path.join(base_path, "openclaw_docs_repo")
    # GitHub creates a directory like 'project-main' when unzipping
    temp_unzip_dir = os.path.join(base_path, "openclaw-main")
    download_url = "https://github.com/openclaw/openclaw/archive/refs/heads/main.zip"

    print("Starting OpenClaw documentation sync via Zip download...")

    try:
        # 1. Clean up previous versions to ensure a fresh start
        print("Cleaning up old versions...")
        if os.path.exists(repo_dir):
            shutil.rmtree(repo_dir)
        if os.path.exists(temp_unzip_dir):
            shutil.rmtree(temp_unzip_dir)
        if os.path.exists(zip_path):
            os.remove(zip_path)

        # 2. Download the zip file
        print(f"Downloading from {download_url}...")
        subprocess.run(
            ["curl", "-L", "-o", zip_path, download_url],
            check=True, capture_output=True, text=True
        )
        print("Download complete.")

        # 3. Unzip the file
        print(f"Unzipping {zip_path}...")
        subprocess.run(
            ["unzip", "-o", zip_path, "-d", base_path],
            check=True, capture_output=True, text=True
        )
        print("Unzip complete.")

        # 4. Rename the unzipped folder to the final name
        print(f"Renaming '{temp_unzip_dir}' to '{repo_dir}'...")
        os.rename(temp_unzip_dir, repo_dir)
        print("Directory renamed.")

        # 5. Final cleanup
        print(f"Removing temporary zip file: {zip_path}")
        os.remove(zip_path)

        print("\nDocumentation sync successful!")
        print(f"Docs are ready at: {os.path.join(repo_dir, 'docs')}")

    except subprocess.CalledProcessError as e:
        print("\n--- ERROR ---")
        print(f"A command failed with exit code {e.returncode}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        print("Sync failed.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Sync failed.")

if __name__ == "__main__":
    sync_openclaw_docs_zip()
