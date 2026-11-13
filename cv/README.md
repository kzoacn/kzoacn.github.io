# 中英文 CV

- 发布版：[英文 PDF](cv-en.pdf)、[中文 PDF](cv-zh.pdf)。主页始终链接这两个固定文件名。
- [完整压缩包](cv-bundle.zip)：两份 PDF、LaTeX 源码和编译工具。
- `latex/cv-en.tex` 和 `latex/cv-zh.tex`：分别维护英文、中文正文。
- `latex/publications.bib`：共用论文库，修改后同时更新两种语言。
- `latex/cv-style.sty`、`latex/rubric.tex` 和 `latex/photo.jpg`：共用样式、CurVe 排版辅助文件和照片。

保留 LianTze Lim 的 CurVe CV 模板版式及署名；合并原有章节小文件，删除模板示例、未使用的推荐人文件和重复资源。历史日期版本 PDF 保留原链接。

## 编译与同步

需要 XeLaTeX、Biber、latexmk、Python 3 和 make。TeX Live 需含 `curve`、`ctex`、`biblatex-ieee`、`cochineal`、`cabin`、`fontawesome5` 及其依赖；中文使用 TeX Live 自带的 Fandol 字体。

在仓库根目录运行：

```sh
make -C cv
```

此命令编译两份简历、更新 `cv-en.pdf` / `cv-zh.pdf` 并重新生成 `cv-bundle.zip`。解压压缩包后，也可在解压出的 `cv` 目录中运行 `make`；在 Overleaf 中将 `latex` 目录的内容上传，选择 XeLaTeX 及所需语言的主文件。

提交时同时提交正文、论文库、两个 PDF 和压缩包。根目录 `.gitignore` 忽略编译中间文件，保留发布版 PDF 和 ZIP；`make -C cv clean` 仅清理构建产物，不删除发布文件。

## 本次论文核对

- 补入 [PKC 2025 正式论文](https://doi.org/10.1007/978-3-031-91832-2_9)的作者、页码及 DOI。
- 按 [npj Quantum Information 正式记录](https://doi.org/10.1038/s41534-026-01219-w)补全 2026 年论文的卷号、文章号及 DOI。
- 补入 [National Science Review 2026 正式论文](https://doi.org/10.1093/nsr/nwag103)，保留完整作者信息。
