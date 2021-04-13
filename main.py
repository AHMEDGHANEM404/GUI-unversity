<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>home</class>
 <widget class="QMainWindow" name="home">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1183</width>
    <height>727</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">border-color: rgba(85, 255, 255, 100);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="image">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>20</y>
      <width>111</width>
      <height>161</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border:none;
</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="icon">
     <iconset resource="../../myWork/design.qrc">
      <normaloff>icon/logo.png</normaloff>icon/logo.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>110</width>
      <height>330</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="Add">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>340</y>
      <width>131</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>add</string>
    </property>
    <property name="icon">
     <iconset resource="../../myWork/design.qrc">
      <normaloff>icon/add1.jpg</normaloff>icon/add1.jpg</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>30</width>
      <height>30</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="Reports">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>420</y>
      <width>131</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>reports </string>
    </property>
    <property name="icon">
     <iconset resource="../../myWork/design.qrc">
      <normaloff>icon/r3.png</normaloff>icon/r3.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>30</width>
      <height>30</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="Result">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>260</y>
      <width>131</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Resluts</string>
    </property>
    <property name="icon">
     <iconset resource="../../myWork/design.qrc">
      <normaloff>icon/g2.png</normaloff>icon/g2.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>30</width>
      <height>30</height>
     </size>
    </property>
   </widget>
   <widget class="QTabWidget" name="Slider">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>10</y>
      <width>991</width>
      <height>681</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(0, 255, 255);
color: rgb(0, 0, 127);
font: 75 13pt &quot;Arial&quot;;</string>
    </property>
    <property name="currentIndex">
     <number>0</number>
    </property>
    <widget class="QWidget" name="login_3">
     <attribute name="title">
      <string notr="true" comment=" ">Login </string>
     </attribute>
     <widget class="QGroupBox" name="Login">
      <property name="geometry">
       <rect>
        <x>200</x>
        <y>120</y>
        <width>541</width>
        <height>241</height>
       </rect>
      </property>
      <property name="title">
       <string>Login</string>
      </property>
      <widget class="QLineEdit" name="UserName">
       <property name="geometry">
        <rect>
         <x>70</x>
         <y>50</y>
         <width>421</width>
         <height>31</height>
        </rect>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
       <property name="placeholderText">
        <string>User mail</string>
       </property>
      </widget>
      <widget class="QLineEdit" name="Password">
       <property name="geometry">
        <rect>
         <x>70</x>
         <y>130</y>
         <width>421</width>
         <height>31</height>
        </rect>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
       <property name="placeholderText">
        <string>Password</string>
       </property>
      </widget>
      <widget class="QPushButton" name="Log">
       <property name="geometry">
        <rect>
         <x>220</x>
         <y>190</y>
         <width>75</width>
         <height>23</height>
        </rect>
       </property>
       <property name="text">
        <string>Log</string>
       </property>
      </widget>
     </widget>
    </widget>
    <widget class="QWidget" name="SerachSlider">
     <attribute name="title">
      <string>Resluts</string>
     </attribute>
     <widget class="QFrame" name="ResultFrame">
      <property name="geometry">
       <rect>
        <x>100</x>
        <y>100</y>
        <width>711</width>
        <height>341</height>
       </rect>
      </property>
      <property name="frameShape">
       <enum>QFrame::StyledPanel</enum>
      </property>
      <property name="frameShadow">
       <enum>QFrame::Raised</enum>
      </property>
      <widget class="QPushButton" name="SearchBtn">
       <property name="geometry">
        <rect>
         <x>322</x>
         <y>270</y>
         <width>75</width>
         <height>23</height>
        </rect>
       </property>
       <property name="text">
        <string>Search</string>
       </property>
      </widget>
      <widget class="QComboBox" name="Levels">
       <property name="geometry">
        <rect>
         <x>132</x>
         <y>160</y>
         <width>451</width>
         <height>22</height>
        </rect>
       </property>
      </widget>
      <widget class="QComboBox" name="nationality">
       <property name="geometry">
        <rect>
         <x>132</x>
         <y>210</y>
         <width>451</width>
         <height>22</height>
        </rect>
       </property>
      </widget>
      <widget class="QComboBox" name="Department">
       <property name="geometry">
        <rect>
         <x>132</x>
         <y>110</y>
         <width>451</width>
         <height>22</height>
        </rect>
       </property>
      </widget>
      <widget class="QComboBox" name="faculty">
       <property name="geometry">
        <rect>
         <x>130</x>
         <y>60</y>
         <width>451</width>
         <height>22</height>
        </rect>
       </property>
      </widget>
     </widget>
    </widget>
    <widget class="QWidget" name="SearchFrame">
     <attribute name="title">
      <string>search</string>
     </attribute>
     <widget class="QLineEdit" name="SearchBar">
      <property name="geometry">
       <rect>
        <x>260</x>
        <y>90</y>
        <width>301</width>
        <height>31</height>
       </rect>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
      <property name="placeholderText">
       <string>Search by name or id</string>
      </property>
     </widget>
     <widget class="QPushButton" name="SearchBtn_2">
      <property name="geometry">
       <rect>
        <x>700</x>
        <y>90</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="text">
       <string>Search</string>
      </property>
     </widget>
     <widget class="QTableWidget" name="table">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>150</y>
        <width>951</width>
        <height>461</height>
       </rect>
      </property>
      <column>
       <property name="text">
        <string>New Column</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>id</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>name</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>mark</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>New Column</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>mark</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>New Column</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>mark</string>
       </property>
      </column>
     </widget>
     <widget class="QComboBox" name="SreachBy">
      <property name="geometry">
       <rect>
        <x>570</x>
        <y>90</y>
        <width>111</width>
        <height>31</height>
       </rect>
      </property>
      <item>
       <property name="text">
        <string/>
       </property>
      </item>
      <item>
       <property name="text">
        <string>subject code</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>student id</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>subject name</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>subject id</string>
       </property>
      </item>
     </widget>
    </widget>
    <widget class="QWidget" name="addStudent">
     <attribute name="title">
      <string>addStrudents</string>
     </attribute>
     <widget class="QTableWidget" name="table_2">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>110</y>
        <width>951</width>
        <height>541</height>
       </rect>
      </property>
      <column>
       <property name="text">
        <string>New Column</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>id</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>name</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>mark</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>New Column</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>mark</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>New Column</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>mark</string>
       </property>
      </column>
     </widget>
    </widget>
    <widget class="QWidget" name="advanced">
     <attribute name="title">
      <string>settings</string>
     </attribute>
     <widget class="QScrollArea" name="EditBar">
      <property name="geometry">
       <rect>
        <x>9</x>
        <y>30</y>
        <width>961</width>
        <height>611</height>
       </rect>
      </property>
      <property name="widgetResizable">
       <bool>true</bool>
      </property>
      <widget class="QWidget" name="scrollAreaWidgetContents_3">
       <property name="geometry">
        <rect>
         <x>0</x>
         <y>0</y>
         <width>959</width>
         <height>609</height>
        </rect>
       </property>
       <widget class="QGroupBox" name="FacultyDeen">
        <property name="geometry">
         <rect>
          <x>30</x>
          <y>20</y>
          <width>901</width>
          <height>181</height>
         </rect>
        </property>
        <property name="title">
         <string>Faculty Deen</string>
        </property>
        <widget class="QComboBox" name="comboBox_22">
         <property name="geometry">
          <rect>
           <x>290</x>
           <y>50</y>
           <width>531</width>
           <height>22</height>
          </rect>
         </property>
        </widget>
        <widget class="QPushButton" name="pushButton_15">
         <property name="geometry">
          <rect>
           <x>400</x>
           <y>130</y>
           <width>75</width>
           <height>23</height>
          </rect>
         </property>
         <property name="text">
          <string>ok</string>
         </property>
        </widget>
        <widget class="QLabel" name="label_7">
         <property name="geometry">
          <rect>
           <x>120</x>
           <y>50</y>
           <width>101</width>
           <height>21</height>
          </rect>
         </property>
         <property name="text">
          <string>Select</string>
         </property>
        </widget>
       </widget>
       <widget class="QGroupBox" name="DepartmentManger">
        <property name="geometry">
         <rect>
          <x>30</x>
          <y>260</y>
          <width>901</width>
          <height>231</height>
         </rect>
        </property>
        <property name="title">
         <string>Department </string>
        </property>
        <widget class="QComboBox" name="comboBox_23">
         <property name="geometry">
          <rect>
           <x>170</x>
           <y>60</y>
           <width>671</width>
           <height>22</height>
          </rect>
         </property>
        </widget>
        <widget class="QPushButton" name="pushButton_16">
         <property name="geometry">
          <rect>
           <x>380</x>
           <y>170</y>
           <width>75</width>
           <height>23</height>
          </rect>
         </property>
         <property name="text">
          <string>ok</string>
         </property>
        </widget>
        <widget class="QLabel" name="label_8">
         <property name="geometry">
          <rect>
           <x>40</x>
           <y>62</y>
           <width>101</width>
           <height>21</height>
          </rect>
         </property>
         <property name="text">
          <string>Proffessor</string>
         </property>
        </widget>
        <widget class="QComboBox" name="comboBox_24">
         <property name="geometry">
          <rect>
           <x>170</x>
           <y>118</y>
           <width>671</width>
           <height>22</height>
          </rect>
         </property>
        </widget>
        <widget class="QLabel" name="label_9">
         <property name="geometry">
          <rect>
           <x>40</x>
           <y>120</y>
           <width>101</width>
           <height>21</height>
          </rect>
         </property>
         <property name="text">
          <string>Deparment</string>
         </property>
        </widget>
       </widget>
      </widget>
     </widget>
    </widget>
    <widget class="QWidget" name="ReportGraph">
     <attribute name="title">
      <string>Reports</string>
     </attribute>
     <widget class="QWidget" name="widget_3" native="true">
      <property name="geometry">
       <rect>
        <x>90</x>
        <y>110</y>
        <width>851</width>
        <height>391</height>
       </rect>
      </property>
     </widget>
    </widget>
   </widget>
   <widget class="QPushButton" name="Search">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>500</y>
      <width>131</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Search</string>
    </property>
    <property name="icon">
     <iconset resource="../../myWork/design.qrc">
      <normaloff>icon/s1.png</normaloff>icon/s1.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>20</width>
      <height>20</height>
     </size>
    </property>
   </widget>
   <widget class="QPushButton" name="Settings">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>570</y>
      <width>131</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>settings</string>
    </property>
    <property name="icon">
     <iconset resource="../../myWork/design.qrc">
      <normaloff>icon/seting1.png</normaloff>icon/seting1.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>30</width>
      <height>30</height>
     </size>
    </property>
   </widget>
  </widget>
 </widget>
 <resources>
  <include location="../../myWork/design.qrc"/>
 </resources>
 <connections/>
</ui>
