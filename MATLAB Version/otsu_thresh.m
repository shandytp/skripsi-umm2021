function varargout = programTepe(varargin)
% PROGRAMTEPE MATLAB code for programTepe.fig
%      PROGRAMTEPE, by itself, creates a new PROGRAMTEPE or raises the existing
%      singleton*.
%
%      H = PROGRAMTEPE returns the handle to a new PROGRAMTEPE or the handle to
%      the existing singleton*.
%
%      PROGRAMTEPE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in PROGRAMTEPE.M with the given input arguments.
%
%      PROGRAMTEPE('Property','Value',...) creates a new PROGRAMTEPE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before programTepe_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to programTepe_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help programTepe

% Last Modified by GUIDE v2.5 13-Jul-2021 14:50:44

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @programTepe_OpeningFcn, ...
                   'gui_OutputFcn',  @programTepe_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before programTepe is made visible.
function programTepe_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to programTepe (see VARARGIN)

% Choose default command line output for programTepe
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes programTepe wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = programTepe_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pbProses.
function pbProses_Callback(hObject, eventdata, handles)

citra1 = ('D:\Kuliah baru\SMT 8\Coding Skripsi\MATLAB Version\val\no\');
image_folder = citra1;
    filenames = dir(fullfile(image_folder, '*.jpg'));
    total_images = numel(filenames);
    h = waitbar(0,'Memproses data');
    pause(.33)
    
for n = 1:total_images
    disp(total_images);
    fnames = filenames(n).name;
    %fnames = erase(fnames,'*.jpg');
    full_name= fullfile(image_folder, filenames(n).name);
    I = imread(full_name);
    %   I = rgb2gray(I);
    
    level = graythresh(I)

    BW = im2bw(I,level);

    %buat histogram
    %[counts,x] = imhist(I,16);
    %stem(handles.histogram1,x,counts);
    %hist1 = stem(x,counts)
    %imshow(hist1);
    %axes(handles.histogram1);
    
    %komputasi threshold otsutepe
    %T = otsuthresh(counts);
    %BW = imbinarize(I,T);
    %figure
    %axes(handles.hasilotsu);
    %imshow(BW);
    waitbar(n/total_images,h,full_name);
    %fsnames = sprintf('%d',n,'*.jpg');
    write_dir = strcat('D:\Kuliah baru\SMT 8\Coding Skripsi\MATLAB Version\otsu_matlab\val\no\' ,[fnames]);
    imwrite(BW,write_dir);
end

% hObject    handle to pbProses (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
