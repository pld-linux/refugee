Summary:	File encryption utility
Summary(pl):	NarzÍdzie do szyfrowania plikÛw
Name:		refugee
Version:	0.99
Release:	2
License:	GPL
Group:		Applications/File
Group(cs):	Aplikace/Pr·ce se soubory
Group(da):	Programmer/Filer
Group(de):	Applikationen/Datei
Group(es):	Aplicaciones/Archivos
Group(fr):	Applications/Fichiers
Group(is):	Forrit/Skr·atÛl
Group(it):	Applicazioni/File
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•’•°•§•Î
Group(no):	Applikasjoner/Fil
Group(pl):	Aplikacje/Pliki
Group(pt):	AplicaÁıes/Ficheiros
Group(pt_BR):	AplicaÁıes/Arquivos
Group(ru):	“…Ãœ÷≈Œ…—/Ê¡ Ãœ◊Ÿ≈ ’‘…Ã…‘Ÿ
Group(sl):	Programi/Datoteke
Group(sv):	Till‰mpningar/Fil
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Ê¡ Ãœ◊¶ ’‘…Ã¶‘…
Source0:	http://www.synack.com/src/%{name}-%{version}.tar.gz
BuildRequires:	libpng-devel
URL:		http://www.synack.com/soft.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Refugee is a file encryption and steganography utility. It implements
Blowfish and Rijndael in CBC mode and is portable between big- and
little-endian platforms. It supports key sizes from 32-448 bits and
gives the user many ways to make keys. It currently supports hiding
user data in PNG files.

%description -l pl
Refugee to narzÍdzie do szyfrowania plikÛw i steganografii.
Implementuje algorytmy Blowfish i Rijndael w trybie CBC i jest
przeno∂ny miÍdzy platformami typu big- i little-endian. Moøe korzystaÊ
z kluczy od 32 do 448 bitÛw, daj±c przy tym uøytkownikowi wiele
rÛznych sposobÛw na stworzenie klucza. W chwili obecnej refugee
umoøliwia ukrywanie danych uøytkownika w plikach PNG.

%prep
%setup  -q

%build
./setup.sh
%{__make} CFLAGS="%{rpmcflags} -IRijndael \
	-funroll-loops -fomit-frame-pointer \
	-fno-strength-reduce -ffast-math" \
	PNG_LIB="-lpng"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	bindir=%{_bindir}

gzip -9nf BUGS CHANGES CRYPTO README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
