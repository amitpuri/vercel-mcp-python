#!/usr/bin/env python3
"""
Setup script for MCP Client
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up MCP Client...")
    
    # Check if we're in a virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment detected")
    else:
        print("⚠️  No virtual environment detected. Consider using one for better isolation.")
    
    # Install requirements
    if install_requirements():
        print("\n🎉 Setup complete!")
        print("Run the client with: python mcp_client.py")
    else:
        print("\n❌ Setup failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
