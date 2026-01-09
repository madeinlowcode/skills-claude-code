#!/usr/bin/env python3
"""
Initialize Long-Running Agent structure for a project.
Creates .claude/ directory with progress tracking files.
"""

import os
import argparse
from datetime import datetime

def create_directory_structure(base_path="."):
    """Create the .claude directory structure."""
    claude_dir = os.path.join(base_path, ".claude")
    os.makedirs(claude_dir, exist_ok=True)
    return claude_dir

def create_progress_file(claude_dir, project_name):
    """Create initial progress.md file."""
    content = f"""# {project_name} - Progress Tracker

## Current Session: #1
- **Date**: {datetime.now().strftime("%Y-%m-%d")}
- **Features Completed**: 0/0
- **Status**: Initializing project structure

## Session History

### Session #1 ({datetime.now().strftime("%Y-%m-%d")})
- ✅ Initialized long-running agent structure
- ✅ Created feature list
- ⏳ Ready to begin development

## Known Issues
_None yet_

## Next Priorities
1. Review generated feature list
2. Begin implementation of high-priority features
3. Establish development environment

## Notes
_Add important notes here_
"""
    with open(os.path.join(claude_dir, "progress.md"), "w") as f:
        f.write(content)

def create_features_file(claude_dir, project_name, description):
    """Create initial features.xml file."""
    content = f"""<?xml version="1.0" encoding="UTF-8"?>
<features project="{project_name}" total="0" completed="0">
  
  <!-- 
  Feature Status Values:
  - pending: Not yet started
  - in-progress: Currently being worked on
  - complete: Finished and tested
  - blocked: Cannot proceed (see notes)
  
  Priority Values:
  - high: Core functionality, do first
  - medium: Important but not critical
  - low: Nice to have, do last
  -->
  
  <category name="Core Setup">
    <feature id="FEAT-001" status="pending" priority="high">
      <description>Initial project setup and configuration</description>
      <steps>
        <step>Create project structure</step>
        <step>Install dependencies</step>
        <step>Verify build works</step>
      </steps>
    </feature>
  </category>
  
  <!-- 
  TODO: Generate comprehensive feature list based on:
  {description}
  
  Add categories and features following this pattern.
  Aim for 50-200 features for complex projects.
  -->
  
</features>
"""
    with open(os.path.join(claude_dir, "features.xml"), "w") as f:
        f.write(content)

def create_current_task_file(claude_dir):
    """Create empty current-task.md file."""
    content = """# Current Task

_No task currently assigned._

## To assign a task:
1. Copy a feature from features.xml
2. Add acceptance criteria
3. List files to modify
4. Add technical context
5. Specify completion signal
"""
    with open(os.path.join(claude_dir, "current-task.md"), "w") as f:
        f.write(content)

def create_session_log_file(claude_dir):
    """Create session-log.md file."""
    content = f"""# Session Log - {datetime.now().strftime("%Y-%m-%d")}

## Session Start
- **Time**: {datetime.now().strftime("%H:%M")}
- **Session Number**: #1

## Activity Log

### {datetime.now().strftime("%H:%M")} - Session Initialized
- Created .claude/ directory structure
- Generated initial feature list
- Ready for development

---
_Add entries as work progresses_
"""
    with open(os.path.join(claude_dir, "session-log.md"), "w") as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser(
        description="Initialize Long-Running Agent structure"
    )
    parser.add_argument(
        "--project-name", 
        required=True,
        help="Name of the project"
    )
    parser.add_argument(
        "--description",
        default="",
        help="Project description for feature generation"
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Base path for initialization (default: current directory)"
    )
    
    args = parser.parse_args()
    
    print(f"🚀 Initializing Long-Running Agent structure for: {args.project_name}")
    
    claude_dir = create_directory_structure(args.path)
    print(f"📁 Created .claude/ directory")
    
    create_progress_file(claude_dir, args.project_name)
    print(f"📝 Created progress.md")
    
    create_features_file(claude_dir, args.project_name, args.description)
    print(f"📋 Created features.xml")
    
    create_current_task_file(claude_dir)
    print(f"📌 Created current-task.md")
    
    create_session_log_file(claude_dir)
    print(f"📖 Created session-log.md")
    
    print(f"\\n✅ Initialization complete!")
    print(f"Next steps:")
    print(f"  1. Review and expand features.xml with project requirements")
    print(f"  2. Run orientation phase to begin development")

if __name__ == "__main__":
    main()