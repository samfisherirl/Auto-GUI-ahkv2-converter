#SingleInstance Force
#Requires AutoHotkey v2
#Warn all, Off

G := MyGui_Create()
{
    __New() {
    this.MyGUI := Gui(,"NameHere")

	this.ABBLE_ := this.MyGUI.AddCheckBox("x304 y32 w120 h22", "ABBLE")
	this.ABBLE_.OnEvent("Click", this.ABBLE_click)
	this.element54_ := this.MyGUI.AddComboBox("x174 y119 w120 ", "element54")
	this.element54_.OnEvent("Click", this.element54_click)
	this.Able_ := this.MyGUI.AddMonthCal("x346 y272 w225 h160", "Able")
	this.Able_.OnEvent("Click", this.Able_click)
	this.element17_ := this.MyGUI.AddText("x215 y225 w120 h23", "element17")
	this.element17_.OnEvent("Click", this.element17_click)
	this.element18_ := this.MyGUI.AddUpDown("x167 y280 w17 h20", "element18")
	this.element18_.OnEvent("Click", this.element18_click)
	this.element20_ := this.MyGUI.AddDropDownList("x48 y1 w120 ", "element20")
	this.element20_.OnEvent("Click", this.element20_click)
	}
	ABBLE_click(){
	

		}
	element54_click(){
	

		}
	Able_click(){
	

		}
	element17_click(){
	

		}
	element18_click(){
	

		}
	element20_click(){
	

		}
}

