import sys
import Foundation
import AVFoundation

def cut_video(input_path, output_path, cut_from_end_sec):
    url = Foundation.NSURL.fileURLWithPath_(input_path)
    asset = AVFoundation.AVURLAsset.assetWithURL_(url)
    
    duration = asset.duration()
    duration_sec = duration.value / duration.timescale
    print(f"Original duration: {duration_sec} sec")
    
    new_duration_sec = duration_sec - cut_from_end_sec
    if new_duration_sec <= 0:
        print("Cut length is longer than the video!")
        return
        
    # CMTimeMakeWithSeconds is not always exposed directly, we can use CMTimeMake
    start_time = AVFoundation.CMTimeMake(0, 600)
    end_time = AVFoundation.CMTimeMake(int(new_duration_sec * 600), 600)
    time_range = AVFoundation.CMTimeRangeMake(start_time, end_time)
    
    export_session = AVFoundation.AVAssetExportSession.alloc().initWithAsset_presetName_(
        asset, AVFoundation.AVAssetExportPresetHighestQuality)
    export_session.setOutputURL_(Foundation.NSURL.fileURLWithPath_(output_path))
    export_session.setOutputFileType_(AVFoundation.AVFileTypeQuickTimeMovie)
    export_session.setTimeRange_(time_range)
    
    # We need a callback or just check status
    def handler():
        pass
    
    export_session.exportAsynchronouslyWithCompletionHandler_(handler)
    # wait for completion
    while export_session.status() == AVFoundation.AVAssetExportSessionStatusExporting or \
          export_session.status() == AVFoundation.AVAssetExportSessionStatusWaiting:
        Foundation.NSRunLoop.currentRunLoop().runUntilDate_(Foundation.NSDate.dateWithTimeIntervalSinceNow_(0.1))
        
    if export_session.status() == AVFoundation.AVAssetExportSessionStatusCompleted:
        print(f"Successfully saved to {output_path}")
    else:
        print(f"Export failed: {export_session.error()}")

if __name__ == '__main__':
    cut_video(sys.argv[1], sys.argv[2], float(sys.argv[3]))
