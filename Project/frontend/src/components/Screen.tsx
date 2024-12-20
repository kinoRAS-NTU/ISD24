import type { FC, HTMLAttributes } from 'react'
import { useSelector } from 'react-redux'

import type { State } from '@/types/state'

interface ScreenProps extends HTMLAttributes<HTMLImageElement> {
    height: number
    width: number
}

const Screen: FC<ScreenProps> = ({ height, width, style, ...restProps }) => (
    <img
        src={`/video_feed?outline=${useSelector((state: State) => state.outline)}`}
        height={height}
        width={width}
        style={{ borderRadius: 6, ...style }}
        {...restProps}
    />
)

export default Screen
