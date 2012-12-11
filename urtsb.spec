%define debug_package	%{nil}
%define         oname UrTSB
Summary:        Game Server Browser for the FPS Urban Terror
Name:           urtsb
Version:        0.4
Release:        %mkrel 1
License:        GPLv3
Group:          Games/Other
Source0:        http://urtsb.googlecode.com/files/%{oname}-%{version}.tar.gz
Url:            http://code.google.com/p/%{name}/
BuildRequires:  python-devel >= 2.6
Requires:       pygtk2.0

%description
UrTSB is a Game Server Browser for the First Person Shooter game Urban Terror 
(http://www.urbanterror.info), targeted to run on Linux and Windows.

Features:

* Server search (master server query)
* Filter results (including UrT specific game types)
* Display server details - players (with kills, ping) and server vars
* Manage favorites - add/remove servers to a favorites list
* Buddy list - manage a buddy list and search servers your buddies are playing 
  on (note: the search is case sensitive!). Supports sub-strings. For example 
  if you add only the string [clan-tag] a buddy search will return all servers
  where players with [clan-tag] in their name are playing. Good to see where 
  your clan m8s are playing :)
* of course launching Urban Terror with automatic connection to a selected 
  server
* view a list of servers you recently played on (if UrTSB was used to connect) 
  including date of last connection and number of connections
* RCON feature


%prep 
%setup -qn %{oname}-%{version}

%build
OVERRIDE_CFLAGS="%{optflags}" python setup.py build


%install
rm -rf %{buildroot}
#python setup.py install --skip-build --root %{buildroot} \
python setup.py install --skip-build --root=%{buildroot} \
                        --prefix=%{_prefix} \

#Icon installation
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -p %{name}_src/resource/icons/logo.png       %{buildroot}%{_datadir}/pixmaps/%{name}.png

#Menu entry creation
%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__cat} > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{oname}
Comment=Game Server Browser for the FPS Urban Terror
GenericName=Game Server Browser for the FPS Urban Terror
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=ArcadeGame;
EOF


#%find_lang %name --all-name

%files
# -f %{name}.lang
%{_bindir}/%{name}
%{python_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
