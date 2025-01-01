import argparse
import os
from enum import Enum

import yaml


class GPM:
    # i will think about storing the config later
    # config_file = "~/.gpm/config.yaml"
    config_file = "sample_config.yaml"

    def __init__(self):
        self.init_parser()

    def init_parser(self):
        self.parser = argparse.ArgumentParser(
                    prog='Git Profile Manager',
                    description='Managing multiple git profiles with ease',
                    epilog='Text at the bottom of help')
        
        self.parser.add_argument('action', choices=['get', 'set', 'edit'])
    
    def read_config(self):
        with open(self.config_file) as config:
            try:
                return yaml.safe_load(config)
            except yaml.YAMLError as exc:
                print(exc)

    def get_profiles(self):
        profiles = []
        for profile_name, profile in self.read_config()["profiles"].items():
            profiles.append((profile_name, profile))
        
        return profiles
    
    def print_profiles(self):
        for profile in self.get_profiles():
            print(f'{profile[0]}:')
            print(f'    {profile[1]['mail']}')
            print(f'    {profile[1]['username']}\n')

    def get_current_profile(self):
        print("Your current active profile:")
        print(f'Username:   {os.popen("git config user.name").read().rstrip()}')
        print(f'Email:      {os.popen("git config user.email").read().rstrip()}')

    def match_profile(self, profile):
        for profilee in self.get_profiles():
            if profilee[0] == profile:
                print(f'Matching profile {profilee[0]}') 

    def set_profile(self, profile):
        self.match_profile(profile)

        

gpm = GPM()
gpm.print_profiles()


