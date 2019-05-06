#!/usr/bin/env python3

import sys
import os
import csv
import itertools
from datetime import datetime

class CSV_Handle:
	'''Class for handling saw reports and storing as csv files on winShare'''
	def __init__(self):
		super().__init__()
		self.files_list = list()
		self.files_location = "/home/pi/Desktop/Reports/"
		self.win_share_location = "/media/windowsshare/"
		self.win_share_maint_log_csv = "Saw_maint_logs.csv"
		self.current_csv = []
		self.csv_header = []
		self.csv_data = []
		#self.csv_file = str()
		
	def fill_file_list(self):
		try:
			files_in_path = os.listdir(self.files_location)
		except FileNotFoundError:
			print("Invalid Directory")
		else:
			self.files_list = files_in_path
			
	def get_files_list(self):
		return self.files_list
		
	def reader(self, has_header):
		s_to_b = lambda x: True if x == 'True' else False
		
		self.current_csv = csv.reader(open(self.csv_file, 'r'))
		if has_header == 'y' or has_header == 'Y':
			self.csv_header = next(self.current_csv)
		for row in self.current_csv:
			#print(row)
			saw = str(row[0])
			date = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
			bar_num = str(row[2]) #False for doesn't or n/a
			crew_name = str(row[3])
			starts = s_to_b(row[4]) #False for no start
			air_filter = s_to_b(row[5]) #False for not swapped
			wrm_gr_top = s_to_b(row[6]) #True for wear
			wrm_gr_side = s_to_b(row[7]) #True for wear
			cltch_drum_cln = s_to_b(row[8]) #False for not clean
			cltch_drum_grsd = s_to_b(row[9]) #False for not greased
			cltch_drum_dmg = s_to_b(row[10]) #False for damage
			cltch_drum_brn = s_to_b(row[11]) #False for burn
			bear_grsd = s_to_b(row[12]) #False for not greased
			bear_worn = s_to_b(row[13]) #True for worn
			bear_bev = s_to_b(row[14]) #False for beveled
			spkt_dmg = s_to_b(row[15]) #True for damaged
			chn_ctch = s_to_b(row[16]) #False for missing or sheared
			bar_cln = s_to_b(row[17]) #False for not cleaned
			bar_dbr = s_to_b(row[18]) #False for not deburred
			sprkp_disc = s_to_b(row[19]) #False for discolored
			sprkp_wet = s_to_b(row[20]) #False for wet
			sprkp_cb = s_to_b(row[21]) #False for carbon buildup
			oil_leak = s_to_b(row[22]) #False for does leak
			gas_leak = s_to_b(row[23]) #False for does leak
			oil_cln = s_to_b(row[24]) #False for isn't clean
			gas_cln = s_to_b(row[25]) #False for isn't clean
			sldr_1 = s_to_b(row[26]) #False for missing
			sldr_2 = s_to_b(row[27]) #False for missing
			pull_crd_fray = s_to_b(row[28]) #False for is frayed
			pull_crd_short = s_to_b(row[29]) #False for is short
			pull_crd_rtact = s_to_b(row[30]) #False for doesn't retract
			misc = str(row[31])
			
			#save csv data to class var self.csv_data
			self.csv_data = [saw, date, bar_num, crew_name, starts, air_filter,
				wrm_gr_top, wrm_gr_side, cltch_drum_cln, cltch_drum_grsd,
				cltch_drum_dmg, cltch_drum_brn, bear_grsd, bear_worn, bear_bev,
				spkt_dmg, chn_ctch, bar_cln, bar_dbr, sprkp_disc, sprkp_wet,
				sprkp_cb, oil_leak, gas_leak, oil_cln, gas_cln, sldr_1, sldr_2,
				pull_crd_fray, pull_crd_short, pull_crd_rtact, misc]
			
			
				
	def writer(self):
		'''take file_input, convert via file_to_csvLine and write into csv'''
		try:
			line_writer = csv.writer(open(self.win_share_location + self.win_share_maint_log_csv, "a"))
		except FileNotFoundError:
			print("Unable to locate csv file")
		else:
			self.reader('n')
			line_writer.writerow(self.csv_data)
		
	def create_csv_header(self):
		header = ['saw', 'date', 'bar number', 'crew name', 'starts', 'air filter',
				'worm gear top wear', 'worm gear side wear', 'clutch drum clean',
				'clutch drum greased', 'clutch drum damage', 'clutch drum burn',
				'bearing greased', 'bearing worn', 'bearing beveled',
				'sprocket damage', 'chain catch', 'bar cleaned', 'bar deburred',
				'sparkplug discolored', 'sparkplug wet', 'sparkplug carbon buildup',
				'oil cap leaks', 'gas cap leaks', 'oil cap clean', 'gas cap clean',
				'slider 1', 'slider 2', 'pull cord fray', 'pull cord short',
				'pull cord retacts', 'misc comments']
		header_writer = csv.writer(open(self.win_share_location + self.win_share_maint_log_csv, "w"))
		header_writer.writerow(header)
		
	def csv_transfer(self):
		'''take maint. file, use writer, delete file'''
		for i in range(len(self.files_list)):
			self.csv_file = self.files_location + self.files_list[i]
			self.writer()
			os.remove(self.files_location + self.files_list[i])
			
	def csv_search_latest(self, saw_num):
		try:
			'''Search csv of maint. logs, finds all with certain saw number'''
			reader = csv.reader(open(self.win_share_location + self.win_share_maint_log_csv, 'r'))
			saw_num_rows = []
			for row in reader:
				if saw_num == row[0]:
					saw_num_rows.append(reader.line_num)
				else:
					next
			'''Go through indexs returned and finds newest date'''
			saw_csv_lines = []
			for i in range(len(saw_num_rows)):
				reader = csv.reader(open(self.win_share_location + self.win_share_maint_log_csv, 'r'))
				saw_csv_lines.append(next(itertools.islice(reader, saw_num_rows[i] - 1, None)))
			#make list of dates
			date_list = []
			for j in range(len(saw_csv_lines)):
				date_list.append(datetime.strptime(saw_csv_lines[j][1], '%Y-%m-%d %H:%M:%S'))
			#get newest date and csv line
			newest = max(date_list).strftime('%Y-%m-%d %H:%M:%S')
			reader = csv.reader(open(self.win_share_location + self.win_share_maint_log_csv, 'r'))
			for row in reader:
				if saw_num == row[0] and newest == row[1]:
					output = row
					break
				else:
					next
			return output
		except:
			output = list(itertools.repeat('', 32))
			return output
		
			
	def test_fcn(self):
		#self.create_csv_header()
		#self.csv_file = "/home/pi/Desktop/Reports/test"
		#self.writer()
		#self.csv_file = "/home/pi/Desktop/Reports/test2"
		#self.writer()
		#self.fill_file_list()
		#self.files_list = ['test']
		#self.csv_transfer()
		self.csv_search_latest('S1')
		pass

#if __name__ == '__main__':
#		run = CSV_Handle()
#		run.test_fcn()
		
		
