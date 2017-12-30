# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/qobitree
# catalog-date 2008-11-30 00:16:40 +0100
# catalog-license lppl
# catalog-version undef
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
%{_texmfdistdir}/tex/latex/qobitree/qobitree.tex
%doc %{_texmfdistdir}/doc/latex/qobitree/README
%doc %{_texmfdistdir}/doc/latex/qobitree/example.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081130-2
+ Revision: 755564
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081130-1
+ Revision: 719420
- texlive-qobitree
- texlive-qobitree
- texlive-qobitree
- texlive-qobitree

