from pathlib import Path

ROOT = Path(".")
FOOTER = """<!-- My Academic Tutor platform footer -->
<footer class="mat-platform-footer">
  <p><strong>Statistics Foundation for University Students</strong></p>
  <p>Course developed by <strong>My Academic Tutor</strong>.</p>
  <p>© 2026 My Academic Tutor. All rights reserved.</p>
</footer>
<style>
.mat-platform-footer{
  max-width:960px;
  margin:34px auto 0;
  padding:22px 34px;
  border-top:1px solid var(--border, #ded9cf);
  color:var(--text2, #5f5f5a);
  font-size:13px;
  line-height:1.65;
}
.mat-platform-footer strong{color:var(--text, #171717);}
@media(max-width:850px){.mat-platform-footer{padding:20px 18px;}}
</style>
"""

for html_file in ROOT.glob("module-*/*.html"):
    if html_file.name == "index.html":
        continue
    text = html_file.read_text(encoding="utf-8")
    if "mat-platform-footer" in text:
        continue
    if "</body>" in text:
        text = text.replace("</body>", FOOTER + "\n</body>")
        html_file.write_text(text, encoding="utf-8")
        print("Updated", html_file)

print("Footer insertion complete.")
