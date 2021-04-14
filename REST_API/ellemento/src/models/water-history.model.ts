import {Entity, model, property} from '@loopback/repository';

@model({settings: {strict: false}})
export class WaterHistory extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  water_history_id?: number;

  @property({
    type: 'number',
    required: true,
  })
  location_id: number;

  @property({
    type: 'number',
    required: true,
  })
  water_level: number;

  @property({
    type: 'number',
    required: true,
  })
  water_temperature: number;

  @property({
    type: 'number',
    required: true,
  })
  batch_id: number;

  @property({
    type: 'date',
    required: true,
  })
  date_time: string;

  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<WaterHistory>) {
    super(data);
  }
}

export interface WaterHistoryRelations {
  // describe navigational properties here
}

export type WaterHistoryWithRelations = WaterHistory & WaterHistoryRelations;
