Files = dir(strcat('F:\\english\\','*.avi'));
LengthFiles = length(Files);
for i = 1:LengthFiles;
    video_file=Files(i).name;
    video=VideoReader(video_file);
    frame_number=floor(video.Duration * video.FrameRate);
    index = frame_number/2;
    image_name=strcat('',num2str(index));
    image_name=strcat(image_name,'.bmp');
    I=read(video,index);                              
    imwrite(I,image_name,'bmp');                   
    I=[];
end