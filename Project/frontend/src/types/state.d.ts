import type { Color, RCObject } from '@/types/drawing'

export type Tool = 'Binding' | 'Flipbook' | 'Triggering' | 'Emission' | 'Trajectory'

export type Stage = 'Idle' | 'Select' | 'Draw'

export type Action =
    | { type: 'SET_TOOL'; payload: Tool }
    | { type: 'SET_STAGE'; payload: Stage }
    | { type: 'SET_CURRENT_OBJECT'; payload: RCObject }
    | { type: 'SET_COLOR'; payload: Color }
    | { type: 'SET_STROKE_WIDTH'; payload: number }
    | { type: 'SET_OUTLINE'; payload: boolean }
    | { type: 'SAVE_FRAME' }
    | { type: 'SAVE_CURRENT_OBJECT' }
    | { type: 'RESET' }

export interface State {
    tool: Tool
    stage: Stage
    color: Color
    strokeWidth: number
    outline: boolean
    currentObject: RCObject
    finishedObjects: {
        Binding: RCObject[]
        Trajectory: RCObject[]
        Flipbook: RCObject[]
        Triggering: RCObject[]
        Emission: RCObject[]
    }
}
