Blockly.Blocks['robot_motor_power'] = {
	init : function() {
		this.setHelpUrl('http://www.example.com/');
		this.setColour(0);
		this.appendValueInput("POWER").setCheck("Number").appendField(
				new Blockly.FieldDropdown([
						[ "Set the power of the A motor to", "A" ],
						[ "Set the power of the B motor to", "B" ] ]),
				"MOTOR");
		this.setPreviousStatement(true);
		this.setNextStatement(true);
		this.setTooltip('');
	}
};

Blockly.Blocks['robot_light'] = {
	init : function() {
		this.setHelpUrl('http://www.example.com/');
		this.setColour(0);
		this.appendValueInput("LIGHT").setCheck("Number").appendField(
				new Blockly.FieldDropdown([
						[ "Turn to Left", "Left" ],
						[ "Turn to Right", "Right" ],
						[ "Turn to Middle", "Middle" ] ]),
				"COLOR");
		this.setPreviousStatement(true);
		this.setNextStatement(true);
		this.setTooltip('');
	}
};

// Blockly.Blocks['robot_turn'] = {
// 	init : function() {
// 		this.setHelpUrl('http://www.example.com/');
// 		this.setColour(0);
// 		this.appendValueInput("LIGHT").setCheck("Number").appendField(
// 				new Blockly.FieldDropdown([
// 						[ "Set the R of LEDs to", "R" ],
// 						[ "Set the G of LEDs to", "G" ],
// 						[ "Set the B of LEDs to", "B" ] ]),
// 				"COLOR");
// 		this.setPreviousStatement(true);
// 		this.setNextStatement(true);
// 		this.setTooltip('');
// 	}
// };

Blockly.Blocks['control_key_down'] = {
	init : function() {
		this.setHelpUrl('http://www.example.com/');
		this.setColour(210);
		this.appendDummyInput().appendField(new Blockly.FieldDropdown([
                        [ "On ↓ key", "DOWN" ],	[ "On ↑ key", "UP" ], 
                        [ "On ← key", "LEFT" ],	[ "On → key", "RIGHT" ] ]), "KEY")
            .appendField(new Blockly.FieldDropdown([ [ "up", "UP" ], [ "down", "DOWN" ] ]), "TYPE");
        
		this.appendStatementInput("STATEMENTS");
		this.setTooltip('');
	}
};