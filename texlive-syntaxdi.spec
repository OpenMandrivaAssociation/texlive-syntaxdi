%global tl_name syntaxdi
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8.2
Release:	%{tl_revision}.1
Summary:	Create railroad syntax diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/syntaxdi
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/syntaxdi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/syntaxdi.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides TikZ styles for creating special syntax diagrams
known as "railroad" diagrams. The package was originally distributed as
part of the schule bundle.

