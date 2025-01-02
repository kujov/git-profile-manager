import sys
import argparse
import os
from enum import Enum

import yaml


class GPM:

    def __init__(self):
        self.config_file = os.path.expanduser("~/.gpm/config.yaml")
        self.sample_config = {
                'profiles': {
                    'default': {
                        'username': 'your_username',
                        'email': 'your_email@example.com'
                    }
                }
            }

        self.init_parser()

    def init_parser(self):
        self.parser = argparse.ArgumentParser(
                    prog='Git Profile Manager',
                    description='Managing multiple git profiles with ease')
        
        self.parser.add_argument('action', help='', choices=['get', 'set', 'edit', 'list'])

        self.parser.add_argument('profile', choices=[profile[0] for profile in self.get_profiles()])
    
    def read_config(self):
        if not os.path.exists(self.config_file):
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as config:
                yaml.dump(self.sample_config, config)

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
            print(f'    {profile[1]["email"]}')
            print(f'    {profile[1]["username"]}\n')

    def get_current_profile(self):
        print("Your current active profile:")
        print(f'Username:   {os.popen("git config user.name").read().rstrip()}')
        print(f'Email:      {os.popen("git config user.email").read().rstrip()}\n')

    def match_profile(self, profile):
        for profilee in self.get_profiles():
            if profilee[0] == profile:
                print(f'Matching profile {profilee[0]}') 

    def set_profile(self, profile):
        self.match_profile(profile)


def main():
    gpm = GPM()

    if len(sys.argv) == 1:
        gpm.get_current_profile()
        gpm.parser.print_help()
        return

    args = gpm.parser.parse_args()

    if args.action == 'get':
        gpm.get_current_profile()
    elif args.action == 'set':
        if args.profile:
            gpm.set_profile(args.profile)
        else:
            print("Error: Profile name is required for 'set' action")
    elif args.action == 'edit':
        os.system(f'vi {gpm.config_file}')
    elif args.action == 'list':
        gpm.print_profiles()

if __name__ == "__main__":
    main()
