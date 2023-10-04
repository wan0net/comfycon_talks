---
title: XFS Deleted File Recovery
meta_title: ""
description: ComfyCon AU 2022 Summer
date: 20/11/2022
categories: ["ComfyCon AU 2022 Summer"]
speakers: Hal Pomeranz

draft: false
---
Unlike EXT file systems, substantial residue remains when files are deleted from an XFS file system. Deleted directory entries with visible inode information remain in the "slack" space of the directory file. Extent data in the inode is still visible, and so on. The real hurdle is lack of reasonable forensic tools for this file system.

Using low-level file system debugging tools, we can examine the available information and locate the deleted file content on disk. This session features a live demo of the process.

<iframe width="560" height="315" src="https://youtu.be/Qw5xzLPYBZw?si=tIDhGnwEDvTNfS4B" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>