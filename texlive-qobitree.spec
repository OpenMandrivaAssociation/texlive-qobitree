Name:		texlive-qobitree
Version:	20170414
Release:	1
Summary:	LaTeX macros for typesetting trees
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/qobitree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qobitree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qobitree.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides commands \branch and \leaf for specifying the elements
of the tree; you build up your tree with those commands, and
then issue the \tree command to typeset the whole.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/qobitree
%doc %{_texmfdistdir}/doc/latex/qobitree

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
