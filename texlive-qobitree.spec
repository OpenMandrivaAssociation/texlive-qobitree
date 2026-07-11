%global tl_name qobitree
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX macros for typesetting trees
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/qobitree
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qobitree.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qobitree.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides commands \branch and \leaf for specifying the elements of the
tree; you build up your tree with those commands, and then issue the
\tree command to typeset the whole.

