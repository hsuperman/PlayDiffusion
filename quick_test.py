"""
Quick test script for PlayDiffusion deployment.
This checks if the model is accessible and prints available methods.
"""

import modal

def test_deployment():
    """Test if the PlayDiffusion model is deployed and accessible."""
    print("🔍 Checking PlayDiffusion deployment on Modal...")
    print("=" * 60)

    try:
        # Try to lookup the deployed model
        PlayDiffusionModel = modal.Cls.lookup("playdiffusion", "PlayDiffusionModel")
        print("✅ SUCCESS! PlayDiffusion model is deployed and accessible!")
        print()
        print("📊 Deployment Info:")
        print("  - App name: playdiffusion")
        print("  - Class: PlayDiffusionModel")
        print()
        print("🎯 Available Methods:")
        print("  1. model.inpaint.remote(...)")
        print("     → Edit speech by replacing words")
        print()
        print("  2. model.tts.remote(...)")
        print("     → Generate speech from text with voice cloning")
        print()
        print("  3. model.rvc.remote(...)")
        print("     → Convert speech to different voice")
        print()
        print("🌐 Web Interface:")
        print("  https://byron-24077--playdiffusion-gradio-app.modal.run")
        print()
        print("📖 Next Steps:")
        print("  1. Open the web interface URL above in your browser")
        print("  2. Try the 'Text to Speech' tab (easiest to test)")
        print("     - Enter some text")
        print("     - Record a short voice sample (3-5 seconds)")
        print("     - Click 'Convert to Speech'")
        print()
        print("⚠️  Note: First request may take 2-3 minutes as the")
        print("   container cold-starts and downloads model weights.")
        print()
        return True

    except Exception as e:
        print("❌ ERROR: Model not found or not accessible")
        print(f"   Details: {e}")
        print()
        print("💡 To deploy the model, run:")
        print("   uv run modal deploy modal_app.py")
        print()
        return False

if __name__ == "__main__":
    raise SystemExit(0 if test_deployment() else 1)
