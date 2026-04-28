# QNAP N8N Downloader Organization and Streamlining Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Keep the functional downloader/reposter pipeline on the QNAP for 24/7 operation, but organize it into a single folder, rebrand it, and streamline the API into 3 endpoints. Archive the old "Hermes" history to GitHub.

**Architecture:** 
1. Archive Hermes agent and history to GitHub.
2. Consolidate all functional downloader files on the QNAP into `/Volumes/Student OS/n8n_downloader`.
3. Update the QNAP API to provide 3 clear endpoints (`/add`, `/facebook`, `/instagram`).
4. Rebrand all code and workflows from "Hermes Master" to "N8N Downloader".

**Tech Stack:** FastAPI, Python, yt-dlp, ffmpeg, GitHub CLI

---

### Task 1: Archive Hermes History to GitHub

**Step 1: Create the archive repository**
Run: `gh repo create hermes-master-archive --public --description "Archive of Hermes Master pipeline history and agents"`

**Step 2: Prepare and Push Hermes files**
Archive the `hermes-agent` folder and original history logs to GitHub.

---

### Task 2: Organize and Rebrand on QNAP

**Step 1: Consolidate files**
Run: `mkdir -p "/Volumes/Student OS/n8n_downloader/n8n"`
Run: `mv "/Volumes/Student OS/yt_downloader"/* "/Volumes/Student OS/n8n_downloader/"`
Run: `mv "/Volumes/Student OS/workflow.json" "/Volumes/Student OS/n8n_downloader/n8n/socials_workflow.json"`
Run: `mv "/Volumes/Student OS/update_workflow.py" "/Volumes/Student OS/n8n_downloader/n8n/update_socials.py"`
Run: `rmdir "/Volumes/Student OS/yt_downloader"`

**Step 2: Streamline API and Rebrand**
**File:** [MODIFY] `/Volumes/Student OS/n8n_downloader/sync_dl_api.py`
1. **Endpoint 1: `POST /add`**: Triggers background download/transcode.
2. **Endpoint 2: `GET /facebook/{videoId}`**: Returns the raw binary for FB.
3. **Endpoint 3: `GET /instagram/{videoId}`**: Returns the MP4 for Cloudinary/IG.
4. **Rebrand**: Replace all "Hermes Master" strings with "N8N Downloader & Reposter".

---

### Task 3: Update n8n Workflow

**Step 1: Update internal workflow names**
**File:** [MODIFY] `/Volumes/Student OS/n8n_downloader/n8n/socials_workflow.json`
Update name to "N8N Downloader & Reposter".

---

### Task 4: Final Cleanup

**Step 1: Remove Hermes Agent from QNAP**
Run: `rm -rf "/Volumes/Student OS/container-station-data/lib/docker/volumes/e45cb0e85303e4e717160641c055719bde377266f7dc96bdb15fc33c35f05844/_data/skills/autonomous-ai-agents/hermes-agent"`

---

### Verification Plan

**Manual Verification**
1. Verify `/Volumes/Student OS/n8n_downloader` contains all functional files.
2. Verify the root of `/Volumes/Student OS` is clean of project files.
3. Test the new `/add`, `/facebook`, and `/instagram` endpoints on the QNAP.
