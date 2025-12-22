import os

# Files smaller than this (in bytes) will be considered placeholders
PLACEHOLDER_SIZE_THRESHOLD = 100
SCREENSHOT_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif")
DIAGRAM_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif")

def scan_repo(base_path):
    all_files = []
    placeholders = []
    screenshots = []
    diagrams = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
            size = os.path.getsize(file_path)

            # Check placeholder
            if size < PLACEHOLDER_SIZE_THRESHOLD:
                placeholders.append(file_path)

            # Check screenshots
            if "screenshots" in root.lower() and file.lower().endswith(SCREENSHOT_EXTENSIONS):
                screenshots.append(file_path)

            # Check diagrams
            if "diagrams" in root.lower() and file.lower().endswith(DIAGRAM_EXTENSIONS):
                diagrams.append(file_path)

    return all_files, placeholders, screenshots, diagrams

def print_report(base_path):
    all_files, placeholders, screenshots, diagrams = scan_repo(base_path)
    total_files = len(all_files)

    placeholder_pct = round(len(placeholders) / total_files * 100, 1) if total_files else 0
    screenshot_pct = round(len(screenshots) / 20 * 100, 1)  # assume 20+ screenshots = full points
    diagram_pct = round(len(diagrams) / 1 * 100, 1)  # assume 1 diagram = full points

    print("\n===== Repo Scan Report =====\n")
    print(f"Total files found: {total_files}\n")

    if placeholders:
        print(f"⚠️ Placeholder / tiny files ({len(placeholders)} | {placeholder_pct}% of total):")
        for f in placeholders:
            print(f"   - {f}")
    else:
        print("✅ No placeholder files detected.")

    print(f"\n📸 Screenshots found ({len(screenshots)} | {screenshot_pct}% of ideal 20+):")
    for s in screenshots:
        print(f"   - {s}")

    print(f"\n📊 Diagrams found ({len(diagrams)} | {diagram_pct}% of ideal 1+):")
    for d in diagrams:
        print(f"   - {d}")

    print("\nAll files scanned successfully.\n")

if __name__ == "__main__":
    base_repo_path = os.path.dirname(os.path.abspath(__file__))
    print_report(base_repo_path)
