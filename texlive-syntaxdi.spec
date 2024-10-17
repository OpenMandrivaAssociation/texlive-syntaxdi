Name:		texlive-syntaxdi
Version:	56685
Release:	2
Summary:	Create "railroad" syntax diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/syntaxdi
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntaxdi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntaxdi.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides TikZ styles for creating special syntax
diagrams known as "railroad" diagrams. The package was
originally distributed as part of the schule bundle.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/syntaxdi
%doc %{_texmfdistdir}/doc/latex/syntaxdi

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
