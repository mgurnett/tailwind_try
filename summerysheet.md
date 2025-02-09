- **Default** 
- Fields: 
	- temparature (IntegerField)
    
- **Chain** 
- Fields: 
	- ip (CharField, max_length=20, unique=True) 
	- description (CharField, max_length=100, blank=True) 
	- name (CharField, max_length=100, unique=True) 
	- latest_update (DateTimeField, default=datetime(2000, 1, 1, 0, 0)) 
- Methods:
	- num_of_sensors(self) 
	- num_of_readings(self) 
	- data_for_graph(self) 
	- highest_current_temp(self)
    
- **Sensor**
- Fields: 
	- wire1_id (CharField, max_length=100, unique=True) 
	- depth (IntegerField) 
	- chain (ForeignKey to Chain model, on_delete=models.CASCADE) 
	- alarm (IntegerField, default=settings.DEFAULT_ALARM) 
- Methods:
	- depth__str(self) 
	- num_of_readings(self) 
	- high_reading(self) 
	- latest_reading(self) 
	- alarm__str(self) 
	- highest_current_temp(self) 
	- data_for_graph(self)
    
- **Reading** 
- Fields: 
	- recorded (DateTimeField) 
	- sensor (ForeignKey to Sensor model, on_delete=models.CASCADE) 
	- value (FloatField) 
	- alarm_state (IntegerField, choices=ALARM_CHOICES, default=0) 
- Methods:
	- value__str(self)

- **templatetage** 
- temp_with_colour__html (value, alarm, alarm_state): #float, int, object:

- date_format(latest_update):

- alarm_state__html(state):

