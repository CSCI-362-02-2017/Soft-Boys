touch currentdirectorycontents.html
echo " " > currentdirectorycontents.html
for entry in ./*
do
cat >> currentdirectorycontents.html << EOF
  $entry
  </br>
EOF
done
xdg-open currentdirectorycontents.html

