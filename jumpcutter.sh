#! /bin/bash
IN=$(echo $@ | sed 's/--input_file /\n--input_file /g' | grep "\-\-input_file" | awk '{print $1,$2}' | sed 's/--input_file //g')
OUT=$(echo $@ | sed 's/--output_file /\n--output_file /g' | grep "\-\-output_file" | awk '{print $1,$2}' | sed 's/--output_file //g')
TEMPFOLDER="TEMP$(date +%s)"
CURDIR=$(pwd)
BACKUPFILE="BACKUP$(date +%s)"

echo "This script can automatically split your videos every x minutes, feed the splited videos into jumpcutter and merge the resulting videos."
echo "Just append all argument you want to be passed to the jumpcutter process"
echo "For example \"echo 00:20:00 | ./jumpcutter.sh --input_file ...\" will set x to 20"
echo "This limits how much memory the jumpcutter process needs"
echo "The script now listens to input:"
read SPLIT

mkdir $TEMPFOLDER

cp $IN $BACKUPFILE

ffmpeg -i $IN -c copy -map 0 -segment_time $SPLIT -f segment -reset_timestamps 1 $TEMPFOLDER/output%03d.mp4

cd $TEMPFOLDER
for FILE in $(ls .)
do
	mv $FILE $IN
	python3 ../jumpcutter.py $@
	mv $OUT $FILE
	echo "file $FILE" >> mylist.txt
done
ffmpeg -f concat -safe 0 -i mylist.txt -c copy $OUT
cd $CURDIR
mv $BACKUPFILE $IN
rm -rf $TEMPFOLDER
